var $currentloop = $('#D');

function playing(elem){
    $(elem).addClass("playing");
    $(elem).css({
            backgroundColor: '#e1e2e4'
        });
    $(elem).animate({
        backgroundColor: 'none'
    }, 4000);
    
}

function checkLoop(elem){
    console.log('hi');
    $(elem).parent().removeClass("playing");
    if ($('#loop').prop('checked') == false){
        $currentloop.stop();
        $currentloop.removeAttr("data-loop");
    }
    if ($(elem).attr('data-loop')){ 
        $(elem)[0].currentTime = 0;
        $(elem)[0].play();
        playing(elem.parent());
    }
}

function setLoop(elem){
    console.log("setloop")
    $currentloop.stop();
    $currentloop.removeAttr("data-loop");
    $currentloop = $(elem);
    $(elem).attr('data-loop','1');
}

$(document).ready(function(){
    $('#playD').on("click", function(){
        if ($('#loop').prop('checked')){
            setLoop($('#D'));
        }
        $('#D')[0].currentTime = 0;
        $('#D')[0].play();
        playing($(this));
    });

    $('#playA').click(function(){
        if ($('#loop').prop('checked')){
            setLoop($('#A'));
        }
        $('#A')[0].currentTime = 0;
        $('#A')[0].play();
        playing($(this));
    });
    $('#playE2').click(function(){
        if ($('#loop').prop('checked')){
            setLoop($('#E2'));
        }
        $('#E2')[0].currentTime = 0;
        $('#E2')[0].play();
        playing($(this));
    });
    $('#playG').click(function(){
        if ($('#loop').prop('checked')){
            setLoop($('#G'));
        }
        $('#G')[0].currentTime = 0;
        $('#G')[0].play();
        playing($(this));
    });
    $('#playB').click(function(){
        if ($('#loop').prop('checked')){
            setLoop($('#B'));
        }
        $('#B')[0].currentTime = 0;
        $('#B')[0].play();
        playing($(this));
    });
    $('#playE4').click(function(){
        if ($('#loop').prop('checked')){
            setLoop($('#E4'));
        }
        $('#E4')[0].currentTime = 0;
        $('#E4')[0].play();
        playing($(this));
    });
});

