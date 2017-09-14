/**
 * Created by yy on 17-7-17.
 */
var time_weight1 = {'_0':15,'_1':15,'_2':10,'_3':10,'_4':10,'_5':10,'_6':20,'_7':30,'_8':40,'_9':60,'_10':70,'_11':80,
                '_12':70,'_13':80,'_14':70,'_15':70,'_16':60,'_17':50,'_18':40,'_19':30,'_20':50,'_21':50,'_22':40,'_23':20,
};
var time_weight2 = {'_0':15,'_1':15,'_2':10,'_3':10,'_4':10,'_5':10,'_6':20,'_7':30,'_8':40,'_9':60,'_10':70,'_11':80,
                '_12':70,'_13':80,'_14':70,'_15':70,'_16':60,'_17':50,'_18':40,'_19':30,'_20':50,'_21':50,'_22':40,'_23':20,
};
$(function () {
  $("select[name='flow_demand']").click(function () {
      var llxqfs = $("select[name='flow_demand']").val();
      if (llxqfs == 1 || llxqfs == 3){
        $("#refersetting").show();
        $("#remaintime").show();
      }else{
          $("#refersetting").hide();
          $("#remaintime").hide();
      }
  });
});
function moni(type) {
    var task_count = $("#task_count").val();
    if (type==1){
        for (var i=0;i<24;i++){
            if (i<10){
                $("#0"+i).val(Math.ceil(task_count*time_weight1['_'+i]/1000))
            }
            else if(i>=10){
                $("#"+i).val(Math.ceil(task_count*time_weight1['_'+i]/1000))
            }
        }
    }
    else if(type==2){
        alert('还没实现!')
    }

}

function currentMoni(type) {
    var task_count = $("#task_count").val();
    if (type==1){
        var myDate = new Date();
        var currentTime = myDate.getHours();
        var totalWeight = 0;
        for (var i=currentTime;i<24;i++){
            totalWeight += time_weight1['_'+i];
        }
        for (var i=currentTime;i<24;i++){
            if (i<10){
                $("#0"+i).val(Math.ceil(task_count*time_weight1['_'+i]/totalWeight))
            }
            else if(i>=10){
                $("#"+i).val(Math.ceil(task_count*time_weight1['_'+i]/totalWeight))
            }
        }
    }
    else if (type==2){
        alert('还没实现!');
    }
}

function checkData() {
    alert('还没实现!');
}

$("select[name='is_control']").click(function () {
    var task_detail = $("select[name='is_control']").val();
    var task_count = $("#task_count").val();
    if (task_detail == 1) {
        $("#time_task").fadeIn();
        $("#time_task").fadeIn('slow');
        $("#time_task").fadeIn(3000);
        for (var i=0;i<24;i++){
            if (i<10){
                $("#0"+i).val(Math.ceil(task_count*time_weight1['_'+i]/1000))
            }
            else if(i>=10){
                $("#"+i).val(Math.ceil(task_count*time_weight1['_'+i]/1000))
            }
        }
    }else if(task_detail == 0){
        $("#time_task").fadeOut();
        $("#time_task").fadeOut('slow');
        $("#time_task").fadeOut(3000);
    }
});

function clearData() {
    for(var i=0;i<24;i++){
        if(i<10){
            $("#0"+i).val(0)
        }else {
            $("#"+i).val(0)
        }
    }
}