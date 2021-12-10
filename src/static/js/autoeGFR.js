window.onload = function()
 			{
 				var Scr = document.getElementById("Scr");
 				var UA = document.getElementById("UA");
 				Scr.onkeyup = function(){
 					if(Scr.value!=""&&/^\d+$/.test(this.value))
 					{
                       UA.onkeyup = function(){
                       if(UA.value!=""&&/^\d+$/.test(this.value))
 					   {
 						var eGFR = document.getElementById("eGFR");
 						eGFR.value = parseFloat(Scr.value)/parseFloat(UA.value);
 						eGFR.value = parseFloat(eGFR.value).toFixed(0);
 					    //BMIzhi.value = String(Number(BMIzhi.value).toFixed(2));
                        }
                        }
 					}
 				}

 			}