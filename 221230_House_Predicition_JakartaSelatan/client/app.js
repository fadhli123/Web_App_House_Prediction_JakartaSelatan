function getKtvalue() {
    var uiKt = document.getElementsByName("uiKt")
    for(var i in uiKt) {
        if(uiKt[i].checked) {
            return parseInt(i)+1;
        }
    }
    return -1;
}

function getKmvalue() {
    var uiKm = document.getElementsByName("uiKm")
    for(var i in uiKm) {
        if(uiKm[i].checked) {
            return parseInt(i)+1;
        }
    }
    return -1;
}

function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var Lt = document.getElementById("uiLt");
    var Lb = document.getElementById("uiLb");
    var Kt = getKtvalue();
    var Km = getKmvalue();
    var garasi = document.getElementById("uiGarasi");
    var estPrice = document.getElementById("uiEstimatedPrice");

    // var url = "http://127.0.0.1:5000/predict_home_price";
    var url = "/api/predict_home_price";

    $.post(url, {
        LT : parseFloat(Lt.value),
        LB : parseFloat(Lb.value),
        KT : Kt,
        KM : Km,
        garasi : garasi.value, 
    },function(data,status) {
        console.log(data.estimated_price);
        estPrice.innerHTML =  `<h2>Rp. ${data.estimated_price.toLocaleString()}</h2>`;
        console.log(status);
    })

}

function onPageLoad() {
    console.log("document loaded");
    //var url = "http://127.0.0.1:5000/get_garasi_status";
    var url = "/api/get_garasi_status";
    $.get(url,function(data,status) {
        console.log("got response for get_garasi_status request")
        if(data) {
            var garasi = data.garasi;
            var uiGarasi = document.getElementById("uiGarasi");
            $('#uiGarasi').empty();
            for(var i in garasi) {
                var opt = new Option(garasi[i]);
                $('#uiGarasi').append(opt);
            }
        }
    });
}

window.onload = onPageLoad;