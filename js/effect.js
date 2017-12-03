var initProgress = function(){  
    music_bar = new scale("#progress-button","#all-progress","#current-progress");  
};  
  
scale = function(btn, bar, cur_bar){  
    console.log($("#all-progress"));

    this.btn = $(btn);  
    this.bar = $(bar);  
    this.cur_bar = $(cur_bar);  
    this.minLength = this.bar.offset().left;  
    this.maxLength = this.minLength + this.bar.width();  
    this.currentX = this.btn.offset().left;  
    this.currentY = this.btn.offset().top;  
    this.init();  
};  
  
scale.prototype = {  
    init : function(){  
        var f = this;  
        document.addEventListener("touchstart", function(e1){  
            e1.preventDefault();  
            document.addEventListener("touchmove", function(e2){  
                var p = e2.touches[0];  
                var moveX = p.clientX;  
                var moveY = p.clientY;  
                if((Math.abs(moveX - f.currentX) < 20) && (Math.abs(moveY - f.currentY) < 20 )){  
                    if(moveX < f.minLength){  
                        f.cur_bar.css("width", "0%");  
                        f.currentX = f.minLength;  
                    }else if(moveX > f.maxLength){  
                        f.cur_bar.css("width","100%");  
                        f.currentX = f.maxLength;  
                    }else{  
                        var percent = ((moveX - f.minLength)*100)/(f.maxLength - f.minLength);  
                        f.cur_bar.css("width",percent+"%");  
                        f.currentX = moveX;  
                    }  
                }  
            });  
        });  
        document.addEventListener("touchend", function(e){  
            document.addEventListener("touchmove",null);  
        });  
    }  
};  
  
$(document).ready(function(){initProgress()});
