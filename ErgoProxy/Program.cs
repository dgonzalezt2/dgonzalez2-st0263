using Microsoft.AspNetCore.Http.Features;

var builder = WebApplication.CreateBuilder(args);
builder.Configuration.AddJsonFile("appsettings.json", optional: true, reloadOnChange: true);

// Agregar servicios necesarios
builder.Services.AddReverseProxy()
    .LoadFromConfig(builder.Configuration.GetSection("ReverseProxy"));

var app = builder.Build();

// Configurar el middleware de YARP
app.UseRouting();

app.Use(async (context, next) =>
        {
            context.Request.HttpContext.Features.Get<IHttpMaxRequestBodySizeFeature>()
                   .MaxRequestBodySize = 1024 * 1024 * 1024; // 30 MB

            await next.Invoke();
        });

app.UseEndpoints(endpoints =>
{
    endpoints.MapReverseProxy();
});

app.Run();
