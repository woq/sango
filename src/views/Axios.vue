<template>
    <div id="btc" class="d-flex justify-content-center align-items-center">
        <table class="table table-striped table-hover table-bordered" style="width: 70vh;">
        <thead>
            <tr>
            <th scope="col">Code</th>
            <th scope="col">Symbol</th>
            <th scope="col">Rate</th>
            <th scope="col">Description</th>
            <th scope="col">Rate_float</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="item in info" v-bind:key="item.id">
                <th scope="row">{{item.code}}</th>
                <th scope="row">{{item.symbol}} </th>
                <th scope="row">{{item['rate']}}</th>
                <th scope="row">{{item['description']}}</th>
            <th scope="row">{{item['rate_float']}}</th>
            </tr>
        </tbody>
        </table>
        <!--<button @click="getBtcData()" class="btn btn-primary">Words</button>-->
    </div>
</template>
<script>
import axios from 'axios';

export default {
  name: 'Axios',
  data(){
      return {
          info: Object,
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
<style>
#btc{
    height: 70vh;
}
a {
    text-decoration: none;
  }
 
.router-link-active {
    text-decoration: none;
  }
</style>