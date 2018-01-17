import cv2
import numpy as np

def question1(image1,image2):

	''' 
	1. Input images

		a. Find two interesting images to use. They should be color, rectangular in shape (NOT square). Pick one that is wide and one tall.
		You might find some classic vision examples here. Or take your own. Make sure the image width or height do not exceed 512 pixels.
		Output: Store the two images as ps0-1-a-1.png and ps0-1-a-2.png inside the output folder
	'''

	image1 = cv2.resize(image1, (128,256))
	image2 = cv2.resize(image2, (256,128))
	cv2.imwrite('output/ps0-1-a-1.png',image1)
	cv2.imwrite('output/ps0-1-a-2.png',image2)

def question2(image1):

	'''
	2. Color  planes
		a. Swap the red and blue pixels of image 1
		Output: Store as ps0-2-a-1.png in the output folder
		b. Create a monochrome image (img1_green) by selecting the green channel of image 1
		Output: ps0-2-b-1.png
		c. Create a monochrome image (img1_red) by selecting the red channel of image 1
		Output: ps0-2-c-1.png
		d. Which looks more like what you’d expect a monochrome image to look like? Would you expect a computer vision algorithm to work on one better than the other?
		Output: Text response in report ps0_report.pdf
	'''

	# Equivalent: b1 = image1[:,:,0] ; g1 = image1[:,:,1] ; r1 = image1[:,:,2]
	b1,g1,r1 = cv2.split(image1) 
	swap = cv2.merge((r1,g1,b1))
	cv2.imwrite('output/ps0-2-a-1.png',swap)
	cv2.imwrite('output/ps0-2-b-1.png',g1)
	cv2.imwrite('output/ps0-2-c-1.png',r1)

	'''
	d. Since there are a lot of red pixels in the image, the monochrome created with the red channel is more lighter since the intensity values are high, (closer to 255) than the one created with the green channel.
	where there are many low intensity pixels(closer to 0). Algorithm will work better with the red channel monochrome image since it has good contrast and brightness, edges and features are visible.
	'''

def question3(image1,image2):

	'''
	3. Replacement of pixels (Note: For this, use the better channel from 2-b/2-c as monochrome versions.)
		a. Take the inner center square region of 100x100 pixels of monochrome version of image 1 and insert them into the center of monochrome version of image 2
		Output: Store the new image created as ps0-3-a-1.png
	'''

	b1,g1,r1 = cv2.split(image1) 
	b2,g2,r2 = cv2.split(image2)

	x_s = int((r1.shape[0]/2) - 50)
	y_s = int((r1.shape[1]/2) - 50)

	x_e = x_s + 100
	y_e = y_s + 100
	
	r2[x_s:x_e,y_s:y_e] = r1[x_s:x_e,y_s:y_e]

	cv2.imwrite('output/ps0-3-a-1.png',r2)

def question4(image1,image2):

	'''
	4. Arithmetic and Geometric operations
		a. What is the min and max of the pixel values of img1_green? What is the mean? What is the standard deviation?  And how did you compute these?
		Output: Text response, with code snippets
		b. Subtract the mean from all pixels, then divide by standard deviation, then multiply by 10 (if your image is 0 to 255) or by 0.05 (if your image ranges from 0.0 to 1.0). Now add the mean back in.
		Output: ps0-4-b-1.png
		c. Shift img1_green to the left by 2 pixels.
		Output: ps0-4-c-1.png
		d. Subtract the shifted version of img1_green from the original, and save the difference image.
		Output: ps0-4-d-1.png (make sure that the values are legal when you write the image so that you can see all relative differences), text response: What do negative pixel values mean anyways?	
	'''

	b1,g1,r1 = cv2.split(image1) 
	mean = np.mean(g1) 
	stddev = np.std(g1)
	print('Min:',np.min(g1))
	print('Max:',np.max(g1))
	print('Mean:',mean)
	print('Standard Deviation:',stddev)

	sub = (((g1-mean)/stddev)*10)+10
	cv2.imwrite('output/ps0-4-b-1.png',sub)

	shift = np.roll(g1,-2,1)
	cv2.imwrite('output/ps0-4-c-1.png',shift)

	diff = cv2.subtract(g1,shift)
	cv2.imwrite('output/ps0-4-d-1.png',diff)

def question5(image1):	

	'''
	5. Noise
		a. Take the original colored image (image 1) and start adding Gaussian noise to the pixels in the green channel. Increase sigma until the noise is somewhat visible.  
		Output: ps0-5-a-1.png, text response: What is the value of sigma you had to use?
		b. Now, instead add that amount of noise to the blue channel.
		Output: ps0-5-b-1.png
		c. Which looks better? Why?
		Output: Text response
	'''
	greennoise_image = image1.copy()
	bluenoise_image = image1.copy()
	gaussian_noise = np.random.normal(0,0.3,image1[:,:,0].shape).astype(np.uint8)
	greennoise_image[:,:,1] = cv2.add(image1[:,:,1],gaussian_noise)
	cv2.imwrite('output/ps0-5-a-1.png',greennoise_image)
	#a. The noise is somewhat visible with sigma value 0.3
	
	bluenoise_image[:,:,0] = cv2.add(image1[:,:,0],gaussian_noise)
	cv2.imwrite('output/ps0-5-b-1.png',bluenoise_image)
	'''
	c. Bluenoise image looks better because the intensity of blue pixels in the image is lesser than that of the green pixels. 
	 Hence adding blue noise was not as effective as adding green noise at the same sigma value.	
	'''
		
def main():
	image1 = cv2.imread('input/4.1.01.tiff')
	image2 = cv2.imread('input/4.1.02.tiff')
	question1(image1,image2)
	question2(image1)
	question3(image1,image2)
	question4(image1,image2)
	question5(image1)

main()