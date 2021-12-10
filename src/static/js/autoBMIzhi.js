window.onload = function()
 			{
 				var tizhong = document.getElementById("tizhong");
 				var shengao = document.getElementById("shengao");
 				tizhong.onkeyup = function(){
 					if(tizhong.value!=""&&/^\d+$/.test(this.value))
 					{
                       shengao.onkeyup = function(){
                       if(shengao.value!=""&&/^\d+$/.test(this.value)){
 						var BMIzhi = document.getElementById("BMIzhi");
 						BMIzhi.value = 10000*parseFloat(tizhong.value)/(parseFloat(shengao.value)*parseFloat(shengao.value));
 						BMIzhi.value = parseFloat(BMIzhi.value).toFixed(2);
 					    //BMIzhi.value = String(Number(BMIzhi.value).toFixed(2));
                        }
                        }
 					}
 				}

 			}