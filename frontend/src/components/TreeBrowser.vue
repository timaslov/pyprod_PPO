<template>
  <div>
    <div
        class="pl-2 pt-2 inline-flex space-x-3"
        :style="{'margin-left': `${depth * 20}px`}"
    >
        <tree-leaf
            @click="chooseArticle()"
            :node="node"
            :path-array="this.pathArray"
        />
        <span
            v-if="ifChildrenExist()"
            class="text-teal-600 cursor-pointer"
            @click="expanded = !expanded"
        >
          {{expanded ? '&#9660;' : '&#10148;'}}
        </span>
    </div>

    <ul v-if="expanded">
      <TreeBrowser
          @changeArticle="sendArtID($event)"
          v-for="child in node.children"
          :key="child.name"
          :node="child"
          :depth="depth + 1"
          :path-array="this.pathArray.slice(1)"
      />
    </ul>
  </div>
</template>

<script>
import treeLeaf from "@/components/TreeLeaf.vue";
export default {
  components: {treeLeaf},

  name: 'TreeBrowser',

  props: {
    node: Object,
    depth: {
      type: Number,
      default: 0,
    },
    pathArray: Array,
  },

  data() {
    return {
      expanded: false,
      nextArray: Array,
    }
  },

  methods: {
    chooseArticle() {
        this.$emit('changeArticle', this.node)
    },
    sendArtID(node) {
      this.$emit('changeArticle', node)
    },
    ifChildrenExist() {
      return this.node.children.length > 0;
    }
  },

  mounted() {
    if (this.pathArray[0] === this.node.slug && this.pathArray.length > 1)
    {
      this.expanded = true
    }
  },
}
</script>

<style scoped>

</style>
