import json

def handler(request):
    """Health check endpoint for Vercel"""
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            "status": "healthy", 
            "message": "Buildvex API is running"
        })
    }
