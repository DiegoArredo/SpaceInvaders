#version 330

// Campos de entrada y salida del fragment shader
in vec2 fragTexCoord;
in vec3 fragPos;
in vec3 fragNormal;

out vec4 outColor;

// Uniforms del fragment shader
uniform vec3 u_shipPos;
uniform bool u_toggleLight;
uniform sampler2D u_texture;

// Constante, dirección en que mira la nave
vec3 u_viewDir = vec3(0.0, 0.0, -1.0);

void main()
{
    // Se le pide calcular intensity implementando el efecto de foco
    // explicado en el enunciado
    // ============================ COMPLETAR ============================

    //siguiendo instrucciones del enunciado: paso a paso para hacer el efecto foco!

    //posicion de la nave y direccion de la luz
    vec3 ligthPos = u_shipPos;//vector rojo - fuente de luz
    vec3 lightDir = vec3(0, 0, -1);

    // se calcula vector normalizado desde la luz al frag para obtener el angulo
    vec3 lightToFragment = normalize(fragPos - ligthPos); //vector morado
    float angle = dot(lightToFragment, lightDir);
  
   //Se usa la funcion dada con las condiciones de min y max entregadas para el Cone, y se usa el angulo calculado c:
    float innerCone = 0.985;
    float outerCone = 0.94;
    float intensity = smoothstep(outerCone, innerCone, angle);



    // ===================================================================
    // Acá se le pide calcular los componentes ambientales y difusos
    // para una luz direccional, como se indica en el enunciado
    // ======================= COMPLETAR el difuso =======================


    // componente ambiental para evitar la oscuridad absoluta
    vec3 ambient = vec3(0.1, 0.1, 0.1);

    //sombreado de Phong
    vec3 norm = normalize(fragNormal);

    // direccion desde el fragmento hacia la nave (fuente de luz)
    vec3 lightDirFrag = normalize(ligthPos - fragPos);

    // se calcula el factor difuso para la cara que mira hacia la nave
    float diffuseFactorShip = max(dot(norm, lightDirFrag), 0.0);

    // direccion de la luz que ilumina las caras superiores
    vec3 lightDirTop = vec3(0.0, 1.0, 0.0);

    // se calcula el factor difuso para las caras superiores
    float diffuseFactorTop = max(dot(norm, lightDirTop), 0.0);

    // se aplica el foco a "las dos camaras" 
    vec3 diffuse = (diffuseFactorShip + diffuseFactorTop) * intensity * vec3(1.0, 1.0, 1.0);


    // ===================================================================
    // Finalmente incluya lo anterior en el color final
    // ======================== COMPLETAR el color ========================

    // se obtiene el color usando la textura
    vec4 textureColor = texture(u_texture, fragTexCoord);

    //se agrega modelo de iluminación Phong
    vec3 totalLight = ambient;
    //detecta el bool del toggle de luz que le pasamos.
    if (u_toggleLight) {
        totalLight += diffuse; // añade el diffuse si esta prendida. c:
    }

    //se multiplica el color de la textura por la luz total
    outColor = vec4(textureColor.rgb * totalLight, textureColor.a);

    // ===================================================================
}
