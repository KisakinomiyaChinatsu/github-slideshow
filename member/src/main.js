import { createApp } from 'vue'
import { Button, Cell, CellGroup, Card, Tabbar, TabbarItem, Field, PullRefresh, List, Empty } from 'vant'
import 'vant/lib/index.css'
import App from './App.vue'
import router from './router'

const app = createApp(App)
app.use(Button)
app.use(Cell)
app.use(CellGroup)
app.use(Card)
app.use(Tabbar)
app.use(TabbarItem)
app.use(Field)
app.use(PullRefresh)
app.use(List)
app.use(Empty)
app.use(router)
app.mount('#app')
