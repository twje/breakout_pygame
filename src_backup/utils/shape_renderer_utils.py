class ShapeRendererUtils:
    @staticmethod
    def rect(renderer, rectangle):
        renderer.rect(
            rectangle.x,
            rectangle.y,
            rectangle.width,
            rectangle.height
        )

    @staticmethod
    def circle(renderer, circle):        
        renderer.circle(
            circle.x,
            circle.y,
            circle.radius
        )
