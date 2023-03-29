<template>
  <div
      class="
      lg:w-[1024px]
      xl:w-[1280px]
      2xl:w-[1536px]
      m-auto
      my-5
    "
  >
    <articleEditor></articleEditor>
  </div>
</template>

<script>
import articleEditor from "@/components/ArticleEditor.vue";
export default {
  name: "ArticleEditorView.vue",
  components: {articleEditor}
}
</script>
