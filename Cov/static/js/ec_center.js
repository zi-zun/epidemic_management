var ec_center = echarts.init(document.getElementById('c2'));
var mydata = [{"name":"上海","value": 318},{"name":"山西","value": 318},]

var dataList = [
];
ec_center_option = {
    tooltip: {
        triggerOn: "click",
        formatter: function(e, t, n) {
            return .5 == e.value ? e.name + "：有疑似病例" : e.seriesName + "<br />" + e.name + "：" + e.value
        }
    },
    visualMap: {
        min: 0,
        max: 1000,
        left: 0,
        bottom: 0,
        showLabel: true,
        textStyle: {
                color: 'white'
           },
//      text: ["高", "低"],
        pieces: [ {
            gt: 10000,
            label: "> 10000 人",
            color: "#7f1100"
        },{
            gte: 1000,
            lt: 10000,
            label: "1000 - 10000 人",
            color: "#ff5428"
        }, {
            gte: 100,
            lte: 1000,
            label: "100 - 1000 人",
            color: "#ff8c71"
        }, {
            gte: 1,
            lt: 99,
            label: "1 - 99 人",
            color: "#ffd768"
        }, {
            value: 0,
            color: "#ffffff"
        }],
        show: true
    },
    geo: {
        map: "china",
        roam: !1,
        scaleLimit: {
            min: 1,
            max: 2
        },
        zoom: 1.20,
        top: 35,
        label: {
            normal: {
                show: !0,
                fontSize: "14",
                color: "rgba(0,0,0,0.7)"
            }
        },
        itemStyle: {
            normal: {
                //shadowBlur: 50,
                //shadowColor: 'rgba(0, 0, 0, 0.2)',
                borderColor: "rgba(0, 0, 0, 0.2)"
            },
            emphasis: {
                areaColor: "#f2d5ad",
                shadowOffsetX: 0,
                shadowOffsetY: 0,
                borderWidth: 0
            }
        }
    },
    series: [{
        name: "确诊病例",
        type: "map",
        geoIndex: 0,
        data: window.dataList
    }]
}
ec_center.setOption(ec_center_option)
