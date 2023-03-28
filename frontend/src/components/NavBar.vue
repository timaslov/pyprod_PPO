<script setup>
import { useAuthStore } from '@/stores/auth.store';
const store = useAuthStore();

function logoutButton() {
  const authStore = useAuthStore();
  authStore.logout();
}
</script>

<template>
  <nav class="bg-gray-300 px-2 py-2.5 dark:bg-gray-900">
    <div class="container flex flex-wrap items-center justify-between mx-auto">
      <div class="flex space-x-2 items-center">
        <router-link to="/">
          <img src="@/assets/cube_logo.png" alt="logo" class="h-20">
        </router-link>
        <span class="text-2xl text-amber-700">PyProd</span>
      </div>

      <div>
        <button
          type="button"
          class="
            p-2
            text-sm
            text-gray-500
            rounded-lg
            md:hidden
            hover:bg-gray-100
          "
          @click="toggleNavbar()"
        >
          <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clip-rule="evenodd"></path></svg>
        </button>
      </div>

      <div
        class="
          w-full
          md:flex
          md:w-auto
        "
        @click="toggleNavbar()"
        v-bind:class="{'hidden': !showMenu, 'flex': showMenu}"
      >
        <ul
          class="
            flex
            flex-col
            p-4
            mt-4
            rounded-lg
            bg-gray-50
            md:flex-row
            md:space-x-8
            md:mt-0
            md:text-sm
            md:font-medium
            md:bg-white
          "
        >
          <li>
            <router-link
              to="/articles"
              class="
                block py-2 pl-3 pr-4 rounded
                md:bg-transparent
                md:p-0
                md:hover:bg-transparent
                md:hover:text-amber-600
                hover:bg-amber-600
                hover:text-white
              "
              :class="{
                'md:text-amber-600 bg-amber-600 text-white' : this.curTab === 'articles',
                'md:text-gray-700' : this.curTab !== 'articles',
              }"
            >
              Статьи
            </router-link>
          </li>

          <li>
            <router-link
                to="/about"
                class="
                block py-2 pl-3 pr-4 rounded
                md:bg-transparent
                md:p-0
                md:hover:bg-transparent
                md:hover:text-amber-600
                hover:bg-amber-600
                hover:text-white
              "
                :class="{
                'md:text-amber-600 bg-amber-600 text-white' : this.curTab === 'about',
                'md:text-gray-700' : this.curTab !== 'about',
              }"
            >
              О проекте
            </router-link>
          </li>

          <li>
            <p
              class="
                block py-2 pl-3 pr-4 rounded
                md:bg-transparent
                md:text-gray-700
                md:p-0
                md:hover:bg-transparent
                md:hover:text-amber-600
                hover:bg-amber-600
                hover:text-white
              "
            >
              {{ "Поиск" }}
            </p>
          </li>
        </ul>
      </div>

      <div
        class="
          w-full
          md:flex
          md:w-auto
        "
         @click="toggleNavbar()"
         v-bind:class="{'hidden': !showMenu, 'flex': showMenu}"
      >
        <ul
          class="
            space-y-2
            flex
            flex-col
            p-4
            md:flex-row
            md:space-x-8
            md:space-y-0
            md:mt-0
          "
          v-if="store.user === null"
        >
          <li>
            <router-link to="/signIn">
              <button
                type="button"
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
                "
              >
                Войти
              </button>
            </router-link>
          </li>

          <li>
            <router-link to="/signUp">
              <button
                type="button"
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
                "
              >
                Зарегистрироваться
              </button>
            </router-link>
          </li>
        </ul>

        <ul
          class="
            space-y-2
            flex
            flex-col
            p-4
            md:flex-row
            md:space-x-8
            md:space-y-0
            md:mt-0
          "
          v-if="store.user !== null"
        >
          <li>
            <p
              class="text-s py-2">
              {{ store.user.email }}
            </p>
          </li>

          <li>
            <router-link to="/">
              <button
                type="button"
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
                "
                @click="logoutButton"
              >
                Выйти
              </button>
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "nav-bar",

  data() {
    return {
      curTab: String,
      showMenu: false,
    }
  },

  methods: {
    toggleNavbar: function(){
      this.showMenu = !this.showMenu;
    },
  },

  watch: {
    $route: function () {
      this.curTab = this.$route.path.split('/')[1];
    }
  },

}
</script>
