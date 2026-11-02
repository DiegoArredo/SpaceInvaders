#version 330

// Campos de entrada y salida del fragment shader
in vec2 fragTexCoord;
in vec3 fragPos;
in vec3 fragNormal;

out vec4 outColor;

// Uniforms del fragment shader
uniform vec3 u_shipPos;
uniform sampler2D u_texture;

// Constante, dirección en que mira la nave
vec3 u_viewDir = vec3(0.0, 0.0, -1.0);

void main()
{
    // Se le pide calcular intensity implementando el efecto de foco
    // explicado en el enunciado
    // ============================ COMPLETAR ============================

    float intensity = 0.7;

    // ===================================================================


    // Acá se le pide calcular los componentes ambientales y difusos
    // para una luz direccional, como se indica en el enunciado
    // ======================= COMPLETAR el difuso =======================

    // componente ambiental para evitar la oscuridad absoluta

    vec3 ambient = vec3(0.1, 0.1, 0.1);
    // vec3 diffuse = ???

    // ===================================================================


    // Finalmente incluya lo anterior en el color final
    // ======================== COMPLETAR el color ========================

    // se obtiene el color usando la textura
    vec4 textureColor = texture(u_texture, fragTexCoord);
    outColor = textureColor;

    // ===================================================================
}
