let quizStarterContainer = document.getElementById('quiz-starter');
let quizContainer = document.getElementById('quiz-container');

let question = document.getElementById('question-quiz');
let quizCheckboxes = document.getElementsByClassName("answer");
let quizAnswers = document.getElementsByClassName("answer_label");

let sortingNextQuestionBtn = document.getElementById("next-btn");
let sortingEndBtn = document.getElementById("end-btn");

let result = document.getElementById('result-finalresult');
let resultGryffindor = document.getElementById('result-gryffindor');
let resultHufflepuff = document.getElementById('result-hufflepuff');
let resultRavenclaw = document.getElementById('result-ravenclaw');
let resultSlytherin = document.getElementById('result-slytherin');
let comment = document.getElementById('result-comment');

let questionsAnswers = quizJSON.questions
let currQuestion;
let selectedAnswer;

let currIndex = 0;
let endIndex = questionsAnswers.length;

let countGryffindor = 0;
let countHufflepuff = 0;
let countRavenclaw = 0;
let countSlytherin = 0;

/* Handle click on Start Sorting button */
$('#sorting-start-btn').click(function () {
    quizStarterContainer.classList.add('hidden');
    quizContainer.classList.remove('hidden');

    setQuestion();
});

/* Handle click on answer label (checking corresponding checkbox + store selected answer) */
$('.answer_label').click(function () {
    var id = $(this).attr('id');
    var cbId = "answer_" + id.split('_')[1];
    var houseId = "answer_" + id.split('_')[1] + "_house";
    document.getElementById(cbId).checked = true;
    for (var i = 0; i < quizCheckboxes.length; i++) {
        if (quizCheckboxes[i].classList.contains(cbId)) {
            quizCheckboxes[i].checked = false;
        }
    }
    selectedAnswer =  document.getElementById(houseId).innerHTML;
});

/* Handle click on answer checkbox (check it and uncheck all others + store selected answer) */
$('.answer').change(function () {
    var id = $(this).attr('id');
    var houseId = id + "_house";
    for (var i = 0; i < quizCheckboxes.length; i++) {
        if (quizCheckboxes[i].id != id) {
            quizCheckboxes[i].checked = false;
        }
    }
    selectedAnswer =  document.getElementById(houseId).innerHTML;
});

/* Handle click on Next Question button : setting next question and store answer value */
$('#next-btn').click(function () {
    switch (selectedAnswer) {
        case 'gryffindor':
            countGryffindor++;
            break;
        case 'hufflepuff':
            countHufflepuff++;
            break;
        case 'ravenclaw':
            countRavenclaw++;
        case 'slytherin':
            countSlytherin++;
    }

    updateAnswers();
    ++currIndex;
    setQuestion();

    if (currIndex == endIndex - 1) {
        sortingNextQuestionBtn.classList.add("hidden");
        sortingEndBtn.classList.remove("hidden");



    }
});


/* Set current question and answers */
function setQuestion(){
    currQuestion = questionsAnswers[currIndex];
    question.innerHTML = (currIndex+1) + '. ' + currQuestion.question;
    setAnswer('1');
    setAnswer('2');
    setAnswer('3');
    setAnswer('4');
}

/* Set current answers and store house value / answer */
function setAnswer(number){
    var name = 'answer_' + number + '_label';
    var value = 'answer_' + number + '_house';
    var index = parseInt(number)-1;
    document.getElementById(name).innerHTML = currQuestion.answers[index].answer;
    document.getElementById(value).innerHTML = currQuestion.answers[index].house;
}

/* Update answer checkboxes to unchecked for new question */
function updateAnswers(){
    for(var i = 0; i < quizCheckboxes.length; i++){
        quizCheckboxes[i].checked = false;
    }
}

/* Convert number to percentage for final house results */
function convertToPercentage(num){
    return parseFloat(((parseInt(num) / endIndex) * 100)).toFixed(2);
}