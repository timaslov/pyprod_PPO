<template>
  <div class="p-10">
    <subject-block :list-name="'Темы'"/>
  </div>

</template>

<script>
import subjectBlock from "@/components/SubjectBlock.vue";
export default {
  name: 'articles-view',

  components: {
    subjectBlock,
  }
}
</script>
