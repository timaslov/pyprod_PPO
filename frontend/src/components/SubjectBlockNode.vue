<template>
  <button class="
          group
          relative
          block
          h-full
          bg-white
          before:absolute
          before:inset-0
          before:rounded-lg
          before:border-2
          before:border-black
          hover:translate-x-2
          hover:-translate-y-2
          h-20"
          @click="showTree()">
    <span class="text-xl font-medium">
      {{title}}
    </span>
  </button>
</template>

<script>
export default {
  name: "subject-block-node",

  props: {
    title: String,
    node: Object},

  methods: {
    showTree() {
      this.$emit('showTree', this.node)
    }
  }
}
</script>

<style scoped>

</style>
