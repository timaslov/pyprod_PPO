<template>
  <div
    class="
      flex
      flex-col
      p-10
      place-items-center
    "
  >
    <form
      class="
        flex
        flex-col
        space-y-10
        place-items-center
        p-10
        border-2
        border-black
        w-[400px]
      "
    >
      <div>
        <h1 class="text-center text-2xl">
          Регистрация
        </h1>
      </div>

      <div class="grid grid-cols-2 place-items-center">
        <label>Имя (логин)</label>

        <input class="border-2">
      </div>

      <div class="grid grid-cols-2 place-items-center">
        <label>Email</label>

        <input class="border-2">
      </div>

      <div class="grid grid-cols-2 place-items-center">
        <label>Пароль</label>

        <input class="border-2">
      </div>

      <div>
        <button class="
                text-white
                bg-amber-600
                hover:bg-amber-800
                duration-300
                focus:ring-4
                focus:outline-none
                focus:ring-blue-300
                font-medium
                rounded-lg
                text-sm
                px-5
                py-2.5
                text-center
                mr-0
                dark:bg-blue-600
                dark:hover:bg-blue-700
                dark:focus:ring-blue-800
              "
        >Зарегистрироваться</button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "registration-view"
}
</script>
