<template>
  <div v-if="pathArray[pathArray.length-1] === node.slug" class="text-blue-500 text-xl cursor-pointer">
    {{ node.title }}
  </div>
  <div v-else class="text-teal-500 text-xl cursor-pointer">
    {{ node.title }}
  </div>
</template>

<script>
export default {
  name: 'tree-leaf',
  props: {
    node: Object,
    pathArray: Array,
  }
}
</script>

<style scoped>

</style>
