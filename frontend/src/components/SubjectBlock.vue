<template>
  <div
    class="
      border-2
      border-black
      rounded-lg
      p-5
    "
    v-show="!isTreeVisible"
  >
    <p class="text-center text-2xl">{{ listName }}</p>

    <div
      class="
        grid
        gap-4
        grid-cols-1
        sm:grid-cols-2
        md:grid-cols-3
        lg:grid-cols-4
        xl:grid-cols-5
        pt-5
      "
    >
      <subject-block-node
        @showTree="
          isTreeVisible = true;
          setArticleToShow($event);
          updateRoute();
          this.findFullRoute(this.treeData, this.ArticleToShow.slug)
        "
        v-for="elem in this.treeData"
          :key="elem"
          :title="elem.title"
          :node="elem"
      />
    </div>
  </div>

  <div class="flex space-x-10">
    <div class="border-2 border-black rounded-lg"
      v-show="isTreeVisible"
      v-if="fullRoute.length > 0"
    >
      <tree-browser
        @changeArticle="
          setArticleToShow($event);
          updateRoute()
        "
        v-for="child in this.treeData"
          :key="child.title"
          :node="child"
          :path-array="fullRoute"
      />
    </div>

    <div
      class="
        flex-1
        border-2
        border-black
        rounded-lg
      "
       v-if="(typeof ArticleToShow) === (typeof {})"
    >
      <article-block :node="ArticleToShow"/>
    </div>
  </div>
</template>

<script>
import subjectBlockNode from "@/components/SubjectBlockNode.vue";
import treeBrowser from "@/components/TreeBrowser.vue";
import articleBlock from "@/components/ArticleBlock.vue";
import axios from "axios";

export default {
  components: {subjectBlockNode, treeBrowser, articleBlock},

  name: "subject-block",

  props: {
    listName: String},

  data() {
    return {
      urlArticleTree: 'http://127.0.0.1:8000/api/web/v1/articles/index/',
      urlArticle: 'http://127.0.0.1:8000/api/web/v1/articles/',
      treeData: [],
      errors: [],
      isTreeVisible: false,
      ArticleToShow: Object,
      fullRoute: [],
    }
  },

  async created() {
    await this.fetchArticleTree(this.urlArticleTree)

    if (this.$route.params.slug !== undefined)
      if (this.$route.params.slug.length > 0){
        await this.fetchArticle(this.urlArticle, this.$route.params.slug)
        this.findFullRoute(this.treeData, this.$route.params.slug[0])
        this.isTreeVisible = true
      }
  },

  methods: {
    findFullRoute(tree, slug) {
      for (const treeNode of tree)
      {
        if (treeNode.slug === slug)
        {
          this.fullRoute.unshift(treeNode.slug)
          return true
        }

        if (this.findFullRoute(treeNode.children, slug) === true)
        {
          this.fullRoute.unshift(treeNode.slug)
          return true
        }
      }
      return false
    },

    setArticleToShow(node) {
      this.ArticleToShow = node
    },

    updateRoute() {
      this.$router.push(`/articles/${this.ArticleToShow.slug}`)
    },

    async fetchArticleTree(url) {
      await axios
          .get(url)
          .then(response => this.treeData.push(...(response.data)))
    },

    async fetchArticle(url, slug) {
      await axios
          .get(url + slug)
          .then(response => this.ArticleToShow = response.data)
    },

  },

  watch: {
    $route: function () {
      if (this.$route.params.slug !== undefined){
        this.fullRoute = []
        this.findFullRoute(this.treeData, this.$route.params.slug[0])
      }
    }
  },

}
</script>
