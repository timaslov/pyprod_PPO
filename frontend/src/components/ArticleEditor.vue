<template>
    <editor
        class="w-full"
        api-key="no-api-key"
        id="id1"
        v-model="content"
    />
  <button
      type="button"
      class="
        text-white
        bg-amber-600
        hover:bg-amber-800
        duration-300
        font-medium
        rounded-lg
        text-sm
        px-5
        py-2.5
        my-5
      "
      @click="this.postArticle">
    Запостить
  </button>

  <div v-html="content"></div>
</template>

<script>
import Editor from '@tinymce/tinymce-vue'
export default {
  name: "ArticleEditor.vue",

  data() {
    return {
      content: '',
    }
  },

  components: {
    'editor': Editor
  },

  methods: {
    postArticle() {
      console.log(this.content)
    }
  },

}
</script>
