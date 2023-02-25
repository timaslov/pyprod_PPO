<template>

  <div class="pl-10 pt-10 pr-10">
    <subject-block
        :list-name="'Темы'"
    />
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
