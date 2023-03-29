<script setup>
import { useAuthStore } from '@/stores/auth.store';
const store = useAuthStore();

function logoutButton() {
  const authStore = useAuthStore();
  authStore.logout();
}
</script>

<template>
  <nav
    class="
      h-[70px]
      min-w-[200px]
      bg-gray-300
    "
  >
    <div
      class="
        container
        flex
        items-center
        justify-between
        mx-auto
        h-full
      "
    >
      <!-- Логотип и надпись слева в широком режиме -->
      <router-link
        to="/"
        class="
          hidden
          md:flex
          space-x-2
          items-center
          min-w-[50px]
          w-[142px]
        "
      >
        <img
          src="@/assets/cube_logo.png"
          alt="logo"
          class="h-[50px] mx-auto"
        >
        <span
          class="text-2xl text-amber-700"
        >
          PyProd
        </span>
      </router-link>

      <!-- Кнопка выпадающего меню слева в сжатом режиме -->
      <button
        id="navMenuButton"
        type="button"
        class="
          flex
          md:hidden
          mx-3
          w-[50px] h-[50px]
          text-sm
          text-gray-500
        "
        @click="toggleNavMenu()"
      >
          <svg
            id="navMenuButtonSVG"
            class="w-10 h-10 m-auto hover:bg-gray-100 rounded-lg"
            fill="currentColor"
            viewBox="0 0 20 20"
          >
            <path
              id="navMenuButtonSVGPath"
              fill-rule="evenodd"
              d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1
                1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
              clip-rule="evenodd"
            >
            </path>
          </svg>
      </button>

      <!-- Навигационное меню для обоих режимов -->
      <div
        id="navMenu"
        class="
          md:flex
          md:w-auto
          w-[150px]
          z-50
        "
        @click="closeNavMenu()"
        v-bind:class="{'hidden': !showMenu, 'absolute pt-[250px]': showMenu}"
      >
        <ul
          class="
            flex
            flex-col
            p-4
            rounded-lg
            bg-gray-300
            md:flex-row
            md:space-x-8
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
            <router-link
                to="/editor"
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
                'md:text-amber-600 bg-amber-600 text-white' : this.curTab === 'editor',
                'md:text-gray-700' : this.curTab !== 'editor',
              }"
            >
              Редактор
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

      <!-- Логотип по центру в сжатом режиме -->
      <router-link
        to="/"
        class="
          flex
          md:hidden
          items-center
          w-[60px]
        "
      >
        <img
          src="@/assets/cube_logo.png"
          alt="logo"
          class="h-[50px]"
        >
      </router-link>

      <!-- Кнопка "Войти" справа в широком режиме -->
      <div
        class="
          hidden
          md:flex
          w-[142px]
        "
      >
        <router-link
          to="/signIn"
          v-if="store.user === null"
          class="mx-auto"
        >
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

        <ul
          v-if="store.user !== null"
          class="
            space-y-2
            flex
            flex-col
            p-4
            md:flex-row
            md:space-x-2
            md:space-y-0
            md:mt-0
          "
        >
          <li>
            <p
              class="text-s py-2">
              {{ store.user.email.slice(0,3) }}
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

      <!-- Иконка "Войти" справа в сжатом режиме -->
      <router-link
        to="/signIn"
        class="
          mx-3
          w-[50px] h-[50px]
          flex
          md:hidden
          hover:border-2
          border-gray-600
          rounded-full
          cursor-pointer
        "
      >
        <div
          class="
            m-auto
            relative
            w-10 h-10
            overflow-hidden
            bg-gray-100
            rounded-full
          "
        >
          <svg
            class="absolute w-12 h-12 text-gray-400 -left-1"
            fill="currentColor"
            viewBox="0 0 20 20"
          >
            <path
              fill-rule="evenodd"
              d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"
              clip-rule="evenodd"
            >
            </path>
          </svg>
        </div>
      </router-link>

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

  created() {
    window.addEventListener("resize", this.resizeHandler);
    window.addEventListener("click", this.clickHandler);
  },

  destroyed() {
    window.removeEventListener("resize", this.resizeHandler);
    window.addEventListener("click", this.clickHandler);
  },

  methods: {
    toggleNavMenu: function(){
      this.showMenu = !this.showMenu;
    },
    closeNavMenu: function(){
      this.showMenu = false;
    },
    resizeHandler() {
      this.closeNavMenu();
    },
    clickHandler(e) {
      // Лютый костыль, который надо убрать
      if (e.target.id !== 'navMenuButton' &&
          e.target.id !== 'navMenuButtonSVG' &&
          e.target.id !== 'navMenuButtonSVGPath')
        this.closeNavMenu();
    },
  },

  watch: {
    $route: function () {
      this.curTab = this.$route.path.split('/')[1];
    },
  },

}
</script>
