<template>
  <div class="about">
    <h1>List of film Categories:</h1>
    <ul>
      <li v-for="item in listItems">
        {{ item.title }}
      </li>
    </ul>
    -end
  </div>

</template>

<!--
<script>
  export default {
    data() {
      return {
        listItems: []
      }
    },
    methods: {
      async getData() {
        const res = await fetch("https://backend-1rbv.onrender.com/api_cinema/list/");
        const finalRes = await res.json();
        this.listItems = finalRes;
        console.log("DATA = " + finalRes);
      }
    },
    mounted() {
      this.getData()
    }
  }
</script>
-->

<script setup>
  import { ref } from 'vue';

  const listItems = ref([]);

  async function getData() {
    const res = await fetch("https://backend-1rbv.onrender.com/api_cinema/list_filmcateg/");
    const finalRes = await res.json();
    listItems.value = finalRes;
  }

 getData()
</script>