<script setup lang="ts">
import planet from '../../assets/planet.png'
</script>

<template>
    <section className="relative">
        <div className="mx-auto max-w-6xl px-4 sm:px-6">
            <div className="pb-12 pt-32 md:pb-20 md:pt-40">
                <div className="pb-12 text-center md:pb-16">
                    <div
                        className="mb-6 border-y [border-image:linear-gradient(to_right,transparent,--theme(--color-slate-300/.8),transparent)1]"
                        data-aos="zoom-y-out"
                    >
                        <div className="-mx-0.5 flex justify-center -space-x-3">

                        </div>
                        <h1
                            className="mb-6 border-y text-5xl font-bold [border-image:linear-gradient(to_right,transparent,--theme(--color-slate-300/.8),transparent)1] md:text-6xl"
                            data-aos="zoom-y-out"
                            data-aos-delay={150}
                            >
                            The website builder you're <br className="max-lg:hidden" />
                            looking for
                        </h1>
                        <div className="mx-auto max-w-3xl">
                            <p
                                className="mb-8 text-lg text-gray-700"
                                data-aos="zoom-y-out"
                                data-aos-delay={300}
                            >
                                Simple is a modern website builder powered by AI that changes
                                how companies create user interfaces together.
                            </p>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </section>
    <section  className="relative before:absolute before:inset-0 before:-z-20 before:bg-gray-900">
        <div className="mx-auto max-w-6xl px-4 sm:px-6">
            <div className="py-12 md:py-20">
                
                   <div className="mx-auto max-w-3xl pb-16 text-center md:pb-20">
                        <h2 className="text-3xl font-bold text-gray-200 md:text-4xl">
                        Simple helps your teams work more efficiently together
                        </h2>
                   </div>
            </div>
            <div className="pb-16 md:pb-20" data-aos="zoom-y-out">
                <div className="text-center">
                    <div className="relative inline-flex rounded-full before:absolute before:inset-0 before:-z-10 before:scale-[.85] before:animate-[pulse_4s_cubic-bezier(.4,0,.6,1)_infinite] before:bg-linear-to-b before:from-blue-900 before:to-sky-700/50 before:blur-3xl after:absolute after:inset-0 after:rounded-[inherit] after:[background:radial-gradient(closest-side,var(--color-blue-500),transparent)]">
                         <v-img
                                className="rounded-full bg-gray-900"
                                :src="planet"
                                :width="400"
                                :height="400"
                                alt="Planet"
                            >
                            </v-img>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<style scoped>

</style>