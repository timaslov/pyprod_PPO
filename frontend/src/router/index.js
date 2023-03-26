import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from "@/stores/auth.store";

import mainView from "@/views/MainView.vue";
import articlesView from "@/views/ArticlesView.vue";
import aboutView from "@/views/AboutView.vue";
import registrationView from "@/views/RegistrationView.vue";
import authenticationView from "@/views/AuthenticationView.vue";


const routes = [
  {
    path: '/',
    component: mainView
  },
  {
    path: '/about',
    component: aboutView
  },
  {
    path: '/signUp',
    component: registrationView
  },
  {
    path: '/signIn',
    component: authenticationView
  },
  {
    path: '/articles',
    component: articlesView
  },
  {
    path: '/articles/:slug+',
    component: articlesView
  },
]

const router = createRouter(
    {
      routes,
      history: createWebHistory(import.meta.env.BASE_URL)
    }
)

export default router;

router.beforeEach(async (to) => {

  //console.log(to);
  const auth = useAuthStore();

   if (auth.user && (to.fullPath === "/signIn" || to.fullPath === "/signUp")) {
     return '/';
   }
});