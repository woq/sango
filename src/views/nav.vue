<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-primary" style="text-decoration: none;">
    <div class="container-fluid">
      <a class="navbar-brand">保链 - 超级纪念版</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link to="/"><a class="nav-link active">主页</a></router-link>
          </li>
          <li class="nav-item">
            <router-link to="/status"><a class="nav-link">运行状态</a></router-link>
          </li>
          <li class="nav-item">
            <router-link to="/about"><a class="nav-link">关于保链</a></router-link>
          </li>
        </ul>

        <span class="badge bg-primary">v1.1-20210525</span>
      </div>
    </div>
  </nav>
  <router-view/>
</template>

<script>
export default {
  name: "nav"
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