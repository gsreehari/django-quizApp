$('#logout-form').submit((e)=>{
    e.preventDefault()
    $.ajax({
        url: 'http://127.0.0.1:8000/api/signout',
        method: 'POST',
        success:(res)=>{
            console.log(res)
            if(res.code == "SOS"){
                window.location.replace("http://127.0.0.1:8000")
            }
        }
    })
})

$('#quiz_complete_form').on('submit',(e)=>{
    e.preventDefault()
    let quizid = $('#quizid').val();
    console.log(quizid)
    $.ajax({
        url: 'http://127.0.0.1:8000/api/quizAttempted',
        method: 'POST',
        data :{"quizId":quizid},
        success:(res)=>{
            data = res.data
            $('#alert-title').html(`<h2>Score</h2>`)
            $('#final_score').html(`<p>You got <b>${data.obtainedScore}</b> out of <b>${data.totalScore}</b></p>`)
            $('.card-actions').html(`<button class="btn btn-sm" onclick = "closeAlertRedirect()">Ok</button>`)
            $('.alert-container').css('display','block')
        }
    })
})


function closeAlertRedirect(){
    $('.alert-container').css('display','none')
    window.location.replace("http://127.0.0.1:8000/home")
}

function closeAlert(){
    $('.alert-container').css('display','none')
}

function startQuiz(quizid){
    $.ajax({
        url: `http://127.0.0.1:8000/api/getQuiz/${quizid}`,
        method: 'GET',
        success:(res)=>{
            data = res.data
            quiz = data.quiz
                $('#alert-title').html(`<h2>Start ${quiz.name}</h2>`)
                if(!data.completed){
                    $('#final_score').html(`<p>Quiz <b>${quiz.name}</b> has <b>${quiz.numberofquestions}</b> Questions.</p>`)
                    $('.card-actions').html(`
                                            <button class="btn btn-sm" onclick = "closeAlert()">Cancel</button>
                                            <button class="btn btn-sm" onclick = "quizPageNavigation(${quizid})">Start</button>`)
                }else{
                    $('#final_score').html(`<p>You have already attempted this quiz.<br>Your score is <b>${data.obtainedScore}</b> out of <b>${data.totalScore}</b></p>`)
                    $('.card-actions').html(`
                                            <button class="btn btn-sm" onclick = "closeAlert()">Ok</button>`)
                }
                $('.alert-container').css('display','block')
        }
    })
    
    
}


function quizPageNavigation(quizid){
    window.location.replace(`http://127.0.0.1:8000/quiz/${quizid}`)
}

// u8912