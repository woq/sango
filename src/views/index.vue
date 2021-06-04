<template>
  <div class="d-flex align-items-center justify-content-center" style="height:70vh;">
    <div class="card" style="width:20rem;height:20rem;">
      <div class="card-header text-center">保链</div>
      <div class="card-body justify-content-center align-items-center text-center">
        <textarea class="form-control text-center" name="url" v-model="links"
                                                                       placeholder="输入单个或多个链接地址
多个链接地址用回车分开" style="height:10rem;"></textarea><br /><button class="btn btn-primary"  @click="postLinks()">提交</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"
export default {
  name: "index",
  data(){
    return{
      links:"",
      Data:"",
    }
  },
  methods: {
    postLinks(){
      axios
          .post('http://127.0.0.1:3001/users',{
            urls:this.links,
          })
          .then(response => {console.log(response.data)})
          .catch(error => alert(error.message));
    },
    getLinks(){
      this.data = this.links.split(/[\s\n]/)
      for (let key in this.data){
        console.log(this.data[key])
        axios
            .get(this.data[key])
            .then(response => {console.log(response.status)})
            .catch(error => alert(error.message));
      }
    }
  }
}
</script>

<style scoped>
a {
  text-decoration: none;
}

.router-link-active {
  text-decoration: none;
}
</style>