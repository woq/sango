<template>
      <div class="d-flex align-items-center justify-content-center" style="height:70vh;">
        <div class="card" style="width:20rem;height:20rem;">
            <div class="card-header text-center">保链</div>
            <div class="card-body justify-content-center align-items-center">
                <form class="text-center" action="add" method="post"><textarea class="form-control text-center" name="url" 
                placeholder="输入单个或多个链接地址
多个链接地址用回车分开" style="height:10rem;"></textarea><br /><button class="btn btn-primary" type="submit">提交</button></form>
            </div>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
}
</script>
<style>
a {
    text-decoration: none;
  }
 
.router-link-active {
    text-decoration: none;
  }
</style>