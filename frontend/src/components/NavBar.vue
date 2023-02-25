<template>
  <div class="
  content-center
  flex flex-row flex-nowrap shrink items-center justify-center space-x-10
  h-[100px] w-full
  bg-teal-500">
    <router-link to="/" class="flex-none w-32">
      <img src="@/assets/logo.png" alt="logo">
    </router-link>

    <router-link to="/articles" class="flex-initial text-xl">Статьи</router-link>

    <router-link to="/about" class="flex-initial text-xl">О проекте</router-link>

    <p class="flex-initial text-xl">{{ "Поиск" }}</p>

    <router-link to="/signUp" class="flex-initial text-xl">Регистрация</router-link>

    <router-link to="/signIn" class="flex-initial text-xl">Войти</router-link>
  </div>
</template>

<script>
export default {
  name: "NavBar"
}
</script>

<style scoped>

</style>
