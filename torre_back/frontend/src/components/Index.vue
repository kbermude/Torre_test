<template>
  <div style="background-color: rgb(163 205 215);">
    <h1>{{ msg }}</h1>
    <h2>Author: Karen Bermudez </h2>
    <ul>
      <li>
        <a
          href="https://vuejs.org"
          target="_blank"
          style="color:black;">
          With Vue
        </a>
      <br>
      <li>
        <a
          href="https://github.com/kbermude/Torre_test.git"
          target="_blank"
          style="color:black;"
        >
          Repo
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'Index',
  data () {
    return {
      msg: 'Welcome to Torre test'
    }
  }
}
</script>

<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
