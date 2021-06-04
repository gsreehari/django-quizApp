$(`.quizform`).on('submit', function(event){
    event.preventDefault();
    var questionid = $(this).find(":submit").data('qid');
    var quizid = $(this).find(":submit").data('quizid');

    

    var checkedVals = $(`.opt${questionid}:checkbox:checked`).map(function() {
        return parseInt(this.value);
    }).get();

    if(checkedVals.length == 0){
        $(".option-error").html("select atleast one option")
        setTimeout(()=>{
            $(".option-error").html("")
        },1000)
        return false;
    }

    $(`.q-${questionid}`).css('display',"none")

    $.ajax({
        url: 'http://127.0.0.1:8000/api/checkAnswer',
        data: {"questionId":questionid, "quizId":quizid, "selectedOptions":checkedVals},
        dataType:'json',
        method: 'GET',
        success:(res)=>{
            $('#score').html(res.score)
            let partial = false;
            res.correct_answers.forEach(element => {
                $(`#ob-${element}`).css('background-color','#81c784')
                if(checkedVals.includes(element)){
                    partial = res.correct_answers.length == 1 ? false : true
                    $(`#question-info-number-${current_index}`).addClass("correct")
                }
                else{
                    partial = res.correct_answers.length == 1 ? false : true
                    $(`#question-info-number-${current_index}`).addClass("incorrect")
                }
            });

            if(partial){
                $(`#question-info-number-${current_index}`).addClass("partial")
            }
        }
    })
});

