var quizStarterContainer = document.getElementById('quiz-starter');
var quizContainer = document.getElementById('quiz-container');
var question = document.getElementById('question-quiz');

var questionsAnswers = quizJSON.questions
var currQuestion;
var currIndex = 0;
var endIndex = questionsAnswers.length;

var countGryffindor = 0;
var countHufflepuff = 0;
var countRavenclaw = 0;
var countSlytherin = 0;

$('#sorting-start-btn').click(function () {
    quizStarterContainer.classList.add('hidden');
    quizContainer.classList.remove('hidden');

    setQuestion();
});

function setQuestion(){
    currQuestion = questionsAnswers[currIndex];
    question.innerHTML = (currIndex+1) + '. ' + currQuestion.question;
    setAnswer('1');
    setAnswer('2');
    setAnswer('3');
    setAnswer('4');
}

function setAnswer(number){
    var name = 'answer' + number + '_label';
    var index = parseInt(number)-1;
    document.getElementById(name).innerHTML = currQuestion.answers[index].answer;
}