using System.Collections;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;
using System.Threading;

public class AnimationCode : MonoBehaviour
{

    public GameObject[] Body;
    List<string> lines;
    int i = 0;
    // Start is called before the first frame update
    void Start()
    {
        lines = System.IO.File.ReadLines("Assets/AnimationFile.txt").ToList();
    }

    // Update is called once per frame
    void Update()
    {
        string[] points = lines[i].Split(',');

        for(int j=0;j<=32;j++){
            float x = float.Parse(points[0+(j*3)])/100;
            float y = float.Parse(points[1+(j*3)])/100;
            float z = float.Parse(points[2+(j*3)])/300;
            Body[j].transform.localPosition = new Vector3(x,y,z);
        }

        i += 1;
        if (i == lines.Count){i=0;}
        Thread.Sleep(30);
    }
}
