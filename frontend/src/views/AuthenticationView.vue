<template>
  <div class="flex flex-col p-10 place-items-center">
    <form class="flex flex-col space-y-10 place-items-center p-10 border-2 border-black w-[400px]">

      <div><h1 class="text-center text-2xl">Аутентификация</h1></div>

      <div class="grid grid-cols-2 place-items-center">
        <label>Логин / Email</label>
        <input class="border-2">
      </div>

      <div class="grid grid-cols-2 place-items-center">
        <label>Пароль</label>
        <input class="border-2">
      </div>

      <div>
        <button class="p-2 border-2 border-teal-500">Войти</button>
      </div>

    </form>
  </div>
</template>

<script>
export default {
  name: "authentication-view"
}
</script>

<style scoped>

</style>
