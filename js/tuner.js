navigator.getUserMedia = navigator.getUserMedia ||
                         navigator.webkitGetUserMedia ||
                         navigator.mozGetUserMedia;

if (navigator.getUserMedia){
    navigator.getUserMedia({audio:true}, 
        function(stream){
            console.log(stream.getAudioTracks());
            analyser = new WebAudioAnalyser(stream)
            console.log(analyser.frequencies())
        },
        function (error){
            console.log(error);
        })
}