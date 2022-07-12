Vue.component("nav-bar", {
    template: `
    <nav class="nav">
        <a href="#" class="nav__item" v-for="link in links">{{link}}</a>
    </nav>
    `,
    data(){
        return {
            links: ["Home", "Contact", "About"]
        };
    }
});

Vue.component("aside-box", {
    template: `
    <aside class="aside">
        <a class="aside__item" href="#" v-for="item in items">
            <i :class="item.icon"></i>
            {{item.text}}
        </a>
    </aside>
    `,
    data(){
        return {
            items: [
                {icon: "fab fa-html5", text: "HTML"},
                {icon: "fab fa-css3", text: "CSS"},
                {icon: "fab fa-js-square", text: "Javascript"},
                {icon: "fab fa-python", text: "Python"},
                {icon: "fab fa-node-js", text: "NodeJS"},
            ]
        };
    }
});

Vue.component("main-blog", {
    template: `
    <section class="section">
        <article class="article" v-for="post in (4)">
            <h1 class="article__title">{{title}}</h1>
            <p class="article__text text--one">{{text}}</p>
            <p class="article__text text--two">{{text}}</p>
            <div class="btn__row">
               <button class="btn">Read More</button> 
            </div>
        </article>
    </section>
    `,
    data(){
        return {
            title: "My Article",
            text: `Lorem ipsum dolor sit amet consectetur adipisicing elit.
            Dolorem cupiditate cumque ullam explicabo molestias quidem quam
            ipsum magni quaerat iure minima nam voluptatem quas, quia ducimus
            numquam, veniam voluptas ab.`
        };
    }
});

Vue.component("social", {
    template: `
    <div class="social">
        <p>Contact With Me</p>
        <div>
            <i :class="icon" v-for="icon in icons"></i>
        </div>
    </div>
    `,
    data(){
        return {
            icons: ["fab fa-facebook", "fab fa-twitter", "fab fa-instagram", "fab fa-codepen", "fab fa-google"]
        };
    }
});

new Vue({
    el: "#app"
});