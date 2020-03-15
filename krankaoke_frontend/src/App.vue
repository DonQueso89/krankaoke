<template>
  <b-container fluid id="app" class="m-0 p-0 mh-100 main-container">
    <b-row>
        <b-col class="col">
            <b-navbar type="dark" variant="dark">
               <b-navbar-nav align="center" class="mr-auto">
                    <b-navbar-brand to="/list">
                        <b-img fluid thumbnail width=100% height=auto src="https://www.onlygfx.com/wp-content/uploads/2016/02/starburst-explosion.png" alt="XPLODE"></b-img>
                    KRaNkaoke</b-navbar-brand>
                    <b-nav-item to="/">Record</b-nav-item>
                    <b-nav-item to="/list">Krankaokes</b-nav-item>
                    <b-nav-item to="/upload">Upload</b-nav-item>
                </b-navbar-nav>
            </b-navbar>
        </b-col>
    </b-row>
    <b-row>
        <b-col class="m-4">
            <router-view></router-view>
        </b-col>
    </b-row>
  </b-container>
</template>
<style scoped>
.main-container {
    background-color: pink;
}
</style>
