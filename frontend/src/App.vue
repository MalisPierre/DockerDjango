<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/filmcateg_list">Categories</router-link> |
    <router-link to="/film_list">Films</router-link>
  </nav>
 <div class="hello">
    <div style="padding:40px;">
      <h1>
        Hello from
        <span style="color:#29558C">Middleware[i</span>
        <span style="color:#AD5353">]nventory</span>
      </h1>
      <p>
        It is good to have you here this is a Simple Page in
        <span class="bg-info">Vue JS</span> and Running on
        <span class="bg-success">Docker Container</span>
      </p>
    </div>
  </div>
  <router-view/>
</template>
<script>
window.Vue = require("vue");
</script>
<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
