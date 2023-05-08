<script setup>
import { Form, Field } from 'vee-validate';
import * as Yup from 'yup';
import { useAuthStore } from '@/stores/auth.store';
const authStore = useAuthStore();

const schema = Yup.object().shape({
  title: Yup.string().required('Title is required'),
  slug: Yup.string().required('Slug is required'),
});
function onSubmit(values) {
  //if (authStore.user === null)
  //  console.log('null user');
  let userEmail = authStore.user.email;
  if(values.parent === undefined || values.parent === "" || values.parent === null)
    values.parent = ""
  console.log(values);
  console.log(userEmail);
}
</script>

<template>
  <div class="flex flex-col p-10 place-items-center">
    <Form
        @submit="onSubmit"
        v-slot="{errors}"
        :validation-schema="schema"
        class="
        flex
        flex-col
        space-y-10
        place-items-center
        p-10 border-2
        border-black
        w-[800px]
      "
    >
      <h1 class="text-center text-2xl">Инфо о статье</h1>

      <div class="grid grid-cols-2 place-items-center">
        <label>Заголовок *</label>
        <Field v-model="this.articleData.title" name="title" class="border-2" />
        <div v-if="errors.title" class="text-red-500">{{ 'Введите заголовок' }}</div>
      </div>

      <div class="grid grid-cols-2 place-items-center">
        <label>Теги</label>
        <Field v-model="this.articleData.tagline" name="tagline" class="border-2" />
      </div>

      <div class="grid grid-cols-2 place-items-center">
        <label>Родитель</label>
        <Field v-model="this.articleData.parent_id" v-slot="{value}" name="parent" as="select" class="border-2 w-[185px]">
          <option value="" selected>Без родителя</option>
          <option v-for="article in this.articles" :key="article.id" :value="article.id">
            {{ article.title }}
          </option>
        </Field>
      </div>

      <div class="grid grid-cols-2 place-items-center">
        <label>Слаг *</label>
        <Field v-model="this.articleData.slug" name="slug" class="border-2" />
        <div v-if="errors.slug" class="text-red-500">{{ 'Введите слаг' }}</div>
      </div>

      <Field name="content" v-model="this.articleData.content">
        <editor
            class="w-full"
            api-key="no-api-key"
            id="id1"
            v-model="this.articleData.content"
            :init="{format:'html'}"
        />
      </Field>


      <div v-html="this.articleData.content"></div>
      <!--
      <button @click="postArticle">В консоль</button>
      -->

      <button
        type="submit"
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
      >
        Запостить
      </button>
    </Form>
  </div>
</template>

<script>
import axios from "axios";
import Editor from '@tinymce/tinymce-vue'
export default {
  name: "ArticleInfoEditor",
  components: {'editor': Editor},
  data() {
    return {
      urlArticles: 'http://127.0.0.1:8000/api/web/v1/articles/',
      articles: [],
      articleData: Object,
    }
  },

  async created() {
    let response1 = await axios
        .get(this.urlArticles)
        .then(response => this.articles.push(...(response.data)))

    let response2
     if (this.$route.params.slug !== undefined)
       if (this.$route.params.slug.length > 0)
         response2 = await this.fetchArticleBySlug(this.$route.params.slug)

    if (response1 && response2){
      for (let i = 0; i < this.articles.length; i++) {
        if (this.articles[i].slug === this.articleData.slug)
            this.articles.splice(i, 1);
      }
    }

  },

  methods: {
    async fetchArticleBySlug(slug) {
      //console.log(slug)
      return await axios
          .get('http://127.0.0.1:8000/api/web/v1/articles/' + slug)
          .then(response => (this.articleData = response.data))
      //console.log(this.articleData)
    },

  },

}
</script>

<style scoped>

</style>