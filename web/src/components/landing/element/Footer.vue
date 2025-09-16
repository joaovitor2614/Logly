<template>
  <v-footer class="bg-grey-darken-4 text-white pa-8">
    <v-container>
      <v-row>
        <!-- Logo + Description -->
        <v-col cols="12" md="3">
          <div class="d-flex align-center mb-2">
            <v-avatar size="32" class="bg-white text-black font-weight-bold mr-2">L</v-avatar>
            <span class="text-h6 font-weight-bold">Logly</span>
          </div>
          <p class="text-body-2">
            Professional geophysical well log visualization platform for the oil & gas industry.
          </p>
        </v-col>

        <!-- Product -->
        <v-col cols="12" md="3">
          <h4 class="text-subtitle-1 font-weight-bold mb-3">Product</h4>
          <v-list density="compact" class="bg-transparent pa-0">
            <v-list-item v-for="item in productLinks" :key="item.text" class="px-0">
              <v-list-item-title>
                <a :href="item.href" class="text-white text-body-2">{{ item.text }}</a>
              </v-list-item-title>
            </v-list-item>
          </v-list>
        </v-col>

        <!-- Company -->
        <v-col cols="12" md="3">
          <h4 class="text-subtitle-1 font-weight-bold mb-3">Company</h4>
          <v-list density="compact" class="bg-transparent pa-0">
            <v-list-item v-for="item in companyLinks" :key="item.text" class="px-0">
              <v-list-item-title>
                <a :href="item.href" class="text-white text-body-2">{{ item.text }}</a>
              </v-list-item-title>
            </v-list-item>
          </v-list>
        </v-col>

        <!-- Support -->
        <v-col cols="12" md="3">
          <h4 class="text-subtitle-1 font-weight-bold mb-3">Support</h4>
          <v-list density="compact" class="bg-transparent pa-0">
            <v-list-item v-for="item in supportLinks" :key="item.text" class="px-0">
              <v-list-item-title>
                <a :href="item.href" class="text-white text-body-2">{{ item.text }}</a>
              </v-list-item-title>
            </v-list-item>
          </v-list>
        </v-col>
      </v-row>

      <!-- Bottom section -->
      <v-divider class="my-6" color="grey-lighten-2"></v-divider>
      <v-row align="center" justify="space-between">
        <span class="text-caption">© 2024 Logly. All rights reserved.</span>
        <div>
          <a v-for="item in policyLinks" :key="item.text" :href="item.href" class="text-caption text-white ml-4">
            {{ item.text }}
          </a>
        </div>
      </v-row>
    </v-container>
  </v-footer>
</template>

<script setup>
const productLinks = [
  { text: "Features", href: "#" },
  { text: "Pricing", href: "#" },
  { text: "API Documentation", href: "#" },
  { text: "Integrations", href: "#" },
];

const companyLinks = [
  { text: "About", href: "#" },
  { text: "Careers", href: "#" },
  { text: "Blog", href: "#" },
  { text: "Contact", href: "#" },
];

const supportLinks = [
  { text: "Help Center", href: "#" },
  { text: "Documentation", href: "#" },
  { text: "Community", href: "#" },
  { text: "Status", href: "#" },
];

const policyLinks = [
  { text: "Privacy Policy", href: "#" },
  { text: "Terms of Service", href: "#" },
  { text: "Cookie Policy", href: "#" },
];
</script>

<style scoped>
a {
  text-decoration: none;
}
a:hover {
  text-decoration: underline;
}
</style>
