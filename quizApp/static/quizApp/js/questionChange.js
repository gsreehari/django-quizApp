var current_index = 1;

$(document).ready(()=>{
    document.getElementById('current-index-number').innerHTML = current_index;
    document.querySelector('.quiz_complete_form').style.display = 'none';
})


function nextQuestion(len){

    if(current_index+1 >= len){
        document.querySelector(`#question-div${current_index}`).style.transform = 'translateX(-820px)' 
        document.querySelector('#next-btn').style.display = 'none';
        document.querySelector('.quiz_complete_form').style.display = 'block';
        current_index++;
        document.getElementById('current-index-number').innerHTML = current_index;
        $(`#question-info-number-${current_index}`).toggleClass("active")
        $(`#question-info-number-${current_index-1}`).toggleClass("active")
        return 0;
    }
    

    if(current_index+1 < len){
        document.querySelector('#prev-btn').style.display = 'block';
        document.querySelector(`#question-div${current_index}`).style.transform = 'translateX(-820px)'
        current_index++;
        document.getElementById('current-index-number').innerHTML = current_index;
        $(`#question-info-number-${current_index}`).toggleClass("active")
        $(`#question-info-number-${current_index-1}`).toggleClass("active")
    }
    
}

function previousQuestion(len){
    document.querySelector('.quiz_complete_form').style.display = 'none';
    if(current_index == 2){
        document.querySelector(`#question-div${current_index-1}`).style.transform = 'translateX(0px)' 
        document.querySelector('#prev-btn').style.display = 'none';
        current_index--;
        document.getElementById('current-index-number').innerHTML = current_index;
        $(`#question-info-number-${current_index}`).toggleClass("active")
        $(`#question-info-number-${current_index+1}`).toggleClass("active")
        return 0;
    }

    if(current_index-1 > 0){
        document.querySelector('#next-btn').style.display = 'block';
        document.querySelector(`#question-div${current_index-1}`).style.transform = 'translateX(0px)'
        current_index--;
        document.getElementById('current-index-number').innerHTML = current_index;
        $(`#question-info-number-${current_index}`).toggleClass("active")
        $(`#question-info-number-${current_index+1}`).toggleClass("active")
    }
}