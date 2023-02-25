<template>
  <div class="bg-teal-500 w-full h-full">
    <h1 class="text-xl text-center">
      {{ this.articleData.title }}
    </h1>
    <p class="text-m text-center">
      {{ this.articleData.content }}
    </p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "article-block",

  props: {node: Object},

  data() {
    return {
      urlData: 'http://127.0.0.1:8000/api/web/v1/articles/',
      articleData: Object,
      errors: [],
    }
  },

  watch: {
    async node() {
      await this.fetchContent()
    }
  },

  async mounted() {
    await this.fetchContent()
  },

  methods: {
    async fetchContent() {
      axios
          .get(this.urlData + this.node.slug)
          .then(response => (this.articleData = response.data))
      // try {
      //   const fetchUrl = this.urlData.concat(this.node.slug)
      //   const response = await fetch(fetchUrl)
      //   this.articleData = await response.json()
      // } catch (error) {
      //   this.errors.push(error)
      // }
    }
  },



}
</script>

<style scoped>

</style>
