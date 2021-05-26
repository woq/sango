<template>
  <div class="about">
    <h1>This is an about page</h1>
  </div>
</template>
<script>
// @ is an alias to /src

export default {
  name: 'About',
}
</script>export default {
  name: 'Axios',
  data:() => ({
    info: 'ddddd',
    }),
}

axios
    .get("https://api.coindesk.com/v1/bpi/currentprice.json")
    .then(response => {this.info = response.data.bpi})
    .catch(error => console.log(error, "error"));