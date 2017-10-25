function dodge(event, object){
    var x=  event.clientX;
    var y = event.clientY;
    var elem = document.getElementById(object);
    var obx = window.getComputedStyle(elem).getPropertyValue("left");
    var oby = window.getComputedStyle(elem).getPropertyValue("top");
    obx = parseInt(obx);
    oby = parseInt(oby);
    deltax = obx + 50 - x;
    deltay = oby + 50 - y;
    // console.log(deltax, deltay)
    // elem.style.left = obx + deltax*0.05 +"px";
    // elem.style.top = oby + deltay*0.05 + "px";
    var count = 1;
    var id = setInterval(function(){
        if (count >= 10){
            clearInterval(id);
            count = 0;
        } else if (count <= 5){
            elem.style.left = obx + deltax*(0.01/count) +"px";
            elem.style.top = oby + deltay*(0.01/count) + "px";
            obx = parseInt(elem.style.left);
            oby = parseInt(elem.style.top)
            count++;
        } else{
            console.log(obx, oby);
            elem.style.left = obx - deltax*(0.01) +"px";
            elem.style.top = oby - deltay*(0.01) + "px";
            obx = parseInt(elem.style.left);
            oby = parseInt(elem.style.top)
            console.log(obx, oby);
            count++;
        }
        
     }, 30)
     // clearInterval(id);
    

}
