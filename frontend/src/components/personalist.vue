<template>
	<div id="personalist">
    <div id="showpersonal">
      <div class="container-fluid">
        <div class="row">
    <div id="cchoose" style="font-size:350%">客户选择：</div>
</div>
<div class="row"> 
  <ul id="linelist" style="list-style-typenone">
  </ul>
  <!-- <div class="col-md-6 col-sm-6 col-xs-12"> -->
  </div>
</div>
</div>
</div>
</template>
<style type="text/css">
  #showpersonal{
    margin-top: 3%;
    margin-left:-12%;
  }
ul {list-style:none;}
li {}
#cchoose{
  margin-left: 12%;
}
#linelist{
  margin-top:10%;
}
#personalist{
  margin-left: 50px;
  margin-right:20px;
}
</style>
<script>
import store from '../store/store.js'

export default {
  name: 'personalist',
  data(){
  	return{
  		line:{
  		},
  		linelist:[],
      device:false,
  	}
  },
  created(){

  },	
  mounted(){
    var self = this
      function isMobile(){
        var ua = navigator.userAgent;
        var ipad = ua.match(/(iPad).*OS\s([\d_]+)/),
            isIphone = !ipad && ua.match(/(iPhone\sOS)\s([\d_]+)/),
            isAndroid = ua.match(/(Android)\s+([\d.]+)/),
            isMobile = isIphone || isAndroid;
        if(isMobile) {
            return true;
        }else {
            return false;
        }
      }
      function arraycontains(arr, obj) {  
        var i = arr.length;  
        while (i--) {  
            if (arr[i] === obj) {  
                return true;  
            }  
        }  
        return false;  
    }  
      this.device = isMobile()
      console.log(this.device)
      var a = this.line = store.state.line
      var b = a.slice(0,2)
      var name1;
      var name2;
      // console.log(b.toString() ===["4","7"])
    // for(var i=0;i<a.length;i++){
      // console.log(a[i])
      // self.linelist.push(a[i])
      // this.linelist += '<li><button onclick="location.assign('../pages/line'+a[i]+'/'+'line'+a[i]+'.html')'+'>'+a[i]+'</button></li>'"
            // this.linelist += '<li><button onclick="location.assign("../pages/line4/line4.html")">'+a[i]+'</button></li>'
              if(b.toString() ===["4","7"].toString()){
                console.log(1112111111)
                name1 = '上海生农生化制品有限公司'
                store.state.factoryname1 = name1
                if(this.device === true){
                            $('#cchoose').css('font-size','30px')
                             $('#cchoose').css('margin-left','10px')
                             $('#cchoose').css('margin-top','8px')
                            this.linelist += '<li><a href="/#/line'+'4'+'" class="button  style="list-style-typenone">'+'<span style="font-size:16px;">'+name1+'</span>'+'</a></li></div>'}
                else {
                      this.linelist += '<li style = "margin-left:400px;"><a href="/#/linecom'+'4'+'" class="button button-large style="list-style-typenone;"">'+'<span style="font-size:23px;">'+ name1 +'</span>'+'</a></li></div>'
                }
    
                name2 = '巴斯夫植物保护有限公司'
                store.state.factoryname2 = name2
                if(this.device === true){
                             $('#cchoose').css('font-size','30px')
                             $('#cchoose').css('margin-left','10px')
                             $('#cchoose').css('margin-top','8px')
                            this.linelist += '<li style="margin-top:20px"><a href="/#/line'+'7'+'" class="button style="list-style-typenone">'+'<span style="font-size:16px;margin-left:13px;">'+ name2 +'</span>'+'</a></li></div>'
                          }
                else{
                      this.linelist += '<li style = "margin-left:1300px;margin-top:-50px;"><a href="/#/linecom'+'7'+'" class="button button-large style="list-style-typenone">'+'<span style="font-size:23px;">'+name2+'</span>'+'</a></li></div>'}

    } 
    else{
    if(arraycontains(a,'4'))
      { name1 = '上海生农生化制品有限公司'
                store.state.factoryname1 = name1
                if(this.device === true){
                            $('#cchoose').css('font-size','30px')
                             $('#cchoose').css('margin-left','10px')
                             $('#cchoose').css('margin-top','8px')
                            this.linelist += '<li><a href="/#/line'+'4'+'" class="button  style="list-style-typenone">'+'<span style="font-size:16px;">'+name1+'</span>'+'</a></li></div>'}
                else {
                      this.linelist += '<li style = "margin-left:900px;"><a href="/#/linecom'+'4'+'" class="button button-large style="list-style-typenone;"">'+'<span style="font-size:23px;">'+ name1 +'</span>'+'</a></li></div>'
                }}
    else if(arraycontains(a,'7')){ 
      console.log(4444)
      name2 = '巴斯夫植物保护有限公司'
                store.state.factoryname2 = name2
                if(this.device === true){
                            $('#cchoose').css('font-size','30px')
                             $('#cchoose').css('margin-left','10px')
                             $('#cchoose').css('margin-top','8px')
                            this.linelist += '<li style="margin-top:20px"><a href="/#/line'+'7'+'" class="button style="list-style-typenone">'+'<span style="font-size:16px;margin-left:13px;">'+ name2 +'</span>'+'</a></li></div>'
                          }
                else{
                      this.linelist += '<li style = "margin-left:900px;margin-top:-50px;"><a href="/#/linecom'+'7'+'" class="button button-large style="list-style-typenone">'+'<span style="font-size:23px;">'+name2+'</span>'+'</a></li></div>'}}
  }

    console.log(this.linelist)
  	 $('#linelist').html(this.linelist)
  },
  methods:{
     // $(ul).children.click(function  (argument) {
     //   // body...
     //  window.location.href('/#/line4')
     // })
  }
  }	
</script>