using UnityEngine;

public class CircleMover : MonoBehaviour
{
    public float moveSpeed = 5f; // Speed at which the circle moves
    public float destroyYPosition = -10f; // Y position at which the circle is destroyed

    void Update()
    {
        // Move the circle down the screen
        transform.Translate(Vector3.down * moveSpeed * Time.deltaTime);

        // Destroy the circle if it moves off-screen
        if (transform.position.y < destroyYPosition)
        {
            Destroy(gameObject);
        }
    }
}

using UnityEngine;

public class CircleSpawner : MonoBehaviour
{
    public GameObject circlePrefab; // Reference to the circle prefab
    public float spawnInterval = 1f; // Time interval between spawns
    public float spawnXMin = -5f; // Minimum X position for spawn
    public float spawnXMax = 5f; // Maximum X position for spawn

    private float timer = 0f;

    void Update()
    {
        timer += Time.deltaTime;

        if (timer >= spawnInterval)
        {
            SpawnCircle();
            timer = 0f;
        }
    }

    void SpawnCircle()
    {
        float spawnX = Random.Range(spawnXMin, spawnXMax);
        Vector3 spawnPosition = new Vector3(spawnX, transform.position.y, 0f);
        Instantiate(circlePrefab, spawnPosition, Quaternion.identity);
    }
}
