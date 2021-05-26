<template>
    <div id="btc">
        <h1>Bitcoin Price Index</h1>
        <p>{{info}}</p>
    </div>
</template>
<script>
import axios from 'axios';


export default {
  name: 'Axios',
  data(){
      return {
          info: 'x1',
      }
  },
  methods: {
      getBtcData(){
        axios
            .get("https://api.coindesk.com/v1/bpi/currentprice.json")
            .then(response => {this.info = response.data.bpi})
            .catch(error => console.log(error, "error"));
      }
  },
  created (){
      this.getBtcData()
  }
}


</script>