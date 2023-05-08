<template>
  <div
      class="
      container
      mx-auto
      my-5
      border-2
      border-gray-300
      rounded-lg
    "
  >
    <h1
        class="
        text-xl
        text-center
      "
    >
      Статьи
    </h1>


    <article-to-edit-l-i
        v-for="(n, index) in this.articles"
        :key="index"
        :article="this.articles[index]"
    >
    </article-to-edit-l-i>
  </div>
</template>

<script>
import ArticleToEditLI from "@/components/UserCases/ArticleToEditLI.vue";
export default {
  name: "MyArticlesView",
  components: {ArticleToEditLI},
  data() {
    return {
      articles:
          [
            {title: "Article 1", id: "1", slug: "frontend"},
            {title: "Article 2", id: "2", slug: "backend"},
            {title: "Article 3", id: "3", slug: "vue"},
            {title: "Article 4", id: "4", slug: "vue_router"},
            {title: "Article 5", id: "5", slug: "python"},
          ],
    }
  },
}
</script>

<style scoped>

</style>